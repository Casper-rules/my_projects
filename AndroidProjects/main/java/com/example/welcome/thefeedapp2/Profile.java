package com.example.welcome.thefeedapp2;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.bumptech.glide.Glide;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class Profile extends AppCompatActivity implements View.OnClickListener{
FirebaseAuth mAuth;
TextView uname,userage,displayName;
Button editBtn,feedBtn;
ImageView pic;
FirebaseDatabase database=FirebaseDatabase.getInstance();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);
        mAuth=FirebaseAuth.getInstance();
        uname=findViewById(R.id.name);
        userage=findViewById(R.id.age);
        displayName=findViewById(R.id.displayName);
        pic=findViewById(R.id.imageView);
        editBtn=findViewById(R.id.editProfile);
        editBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
                Intent intent=new Intent(Profile.this,UserInfo.class);
                startActivity(intent);
            }
        });
        feedBtn=findViewById(R.id.feed);
        feedBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
                Intent intent=new Intent(Profile.this,FeedActivity.class);
                startActivity(intent);
            }
        });
        Uri profileImage;
        FirebaseDatabase database=FirebaseDatabase.getInstance();

        loadUserInformation();


    }

    private void loadUserInformation() {

        final FirebaseUser user=mAuth.getCurrentUser();
        assert user != null;
        String picUrl=user.getPhotoUrl().toString();
        String dispName=user.getDisplayName();
        displayName.setText(dispName);
        Glide.with(this).load(user.getPhotoUrl().toString()).into(pic);

        DatabaseReference name=database.getReference("User Name");
        name.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                String nme=dataSnapshot.getValue(String.class);
                uname.setText(nme);
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {
                Toast.makeText(Profile.this, "Failed To Load", Toast.LENGTH_SHORT).show();
            }
        });
        DatabaseReference age=database.getReference("User Age");
        age.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                String uage=dataSnapshot.getValue(String.class);
                userage.setText(uage);
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {
                Toast.makeText(Profile.this, "Failed to load", Toast.LENGTH_SHORT).show();
            }
        });

    }

    @Override
    protected void onStart() {
        super.onStart();
        if(mAuth.getCurrentUser()==null){
            finish();
            startActivity(new Intent(this,MainActivity.class));
        }
    }
    @Override
    public void onClick(View v) {

    }
}
