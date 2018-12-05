package com.example.welcome.thefeedapp2;

import android.content.Intent;
import android.graphics.Bitmap;
import android.net.Uri;
import android.provider.MediaStore;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.auth.UserProfileChangeRequest;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;
import com.google.firebase.storage.UploadTask;

import java.io.IOException;

public class UserInfo extends AppCompatActivity implements View.OnClickListener{

    private static final int CHOOSEIMAGE = 1;
    ImageView proPic;
    EditText name;
    EditText dispName;
    EditText age;
    Button submit;
    Uri profileImage;
    FirebaseDatabase database=FirebaseDatabase.getInstance();
    FirebaseAuth mAuth;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_info);

        mAuth=FirebaseAuth.getInstance();
        proPic=findViewById(R.id.propic);
        name=findViewById(R.id.name);
        dispName=findViewById(R.id.dispName);
        age=findViewById(R.id.age);
        submit=findViewById(R.id.submit);
        proPic.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                showImageChooser();
            }
        });
        submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                saveUserInfo();
            }
        });
    }

    private void saveUserInfo() {

        String userName=name.getText().toString();
        String userDispName=dispName.getText().toString();
        String userAge=age.getText().toString();
        FirebaseUser usr=mAuth.getCurrentUser();
        if(usr!=null){
            UserProfileChangeRequest profile =new UserProfileChangeRequest.Builder()
                    .setDisplayName(userDispName)
                    .setPhotoUri(Uri.parse(imageUrl))
                    .build()
                    ;
            DatabaseReference displayName=database.getReference("Display Name");
            displayName.setValue(userDispName);
            DatabaseReference user_name=database.getReference("User Name");
            user_name.setValue(userName);
            DatabaseReference age=database.getReference("User Age");
            age.setValue(userAge);
            usr.updateProfile(profile)
                    .addOnCompleteListener(new OnCompleteListener<Void>() {
                        @Override
                        public void onComplete(@NonNull Task<Void> task) {
                            if(task.isSuccessful()){
                                Toast.makeText(UserInfo.this, "profile Updated", Toast.LENGTH_SHORT).show();
                                Intent intent=new Intent(UserInfo.this,Profile.class);
                                startActivity(intent);
                            }
                        }
                    });

        }
    }

    private void showImageChooser(){
        Intent intent=new Intent();
        intent.setType("Image/*");
        intent.setAction(Intent.ACTION_GET_CONTENT);
        startActivityForResult(intent,CHOOSEIMAGE);

    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if(requestCode==CHOOSEIMAGE&&resultCode==RESULT_OK&&data!=null&&data.getData()!=null){
            profileImage=data.getData();
            try {
                Bitmap bitmap= MediaStore.Images.Media.getBitmap(getContentResolver(),profileImage);
                proPic.setImageBitmap(bitmap);
                uploadImageToFirebase();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

    }
    String imageUrl;
    private void uploadImageToFirebase() {
        StorageReference proPicRef= FirebaseStorage.getInstance().getReference("profilePics/"+System.currentTimeMillis()+".jpg");
        if(profileImage!=null){
            proPicRef.putFile(profileImage).addOnSuccessListener(new OnSuccessListener<UploadTask.TaskSnapshot>() {
                @Override
                public void onSuccess(UploadTask.TaskSnapshot taskSnapshot) {

                    imageUrl=taskSnapshot.getDownloadUrl().toString();

                }
            })
            .addOnFailureListener(new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception e) {

                    Toast.makeText(UserInfo.this, "Error uploading image", Toast.LENGTH_SHORT).show();
                }
            });
        }

    }


    @Override
    public void onClick(View v) {

    }
}
