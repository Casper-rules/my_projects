package com.example.welcome.thefeedapp2;

import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseAuthUserCollisionException;

public class Signup extends AppCompatActivity implements View.OnClickListener {
    private FirebaseAuth mAuth;
    EditText uname,email,pass;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signup);
        TextView logIn=findViewById(R.id.textView2);
        logIn.setOnClickListener(this);
        Button signUp=findViewById(R.id.button3);
        signUp.setOnClickListener(this);
        uname=findViewById(R.id.uname);
        email=findViewById(R.id.email);
        pass=findViewById(R.id.pass);
        mAuth = FirebaseAuth.getInstance();
    }
    private void registerUser(){
        String emailId=email.getText().toString();
        String password=pass.getText().toString();
        String userName=uname.getText().toString();
        if(userName.isEmpty()){
            uname.setError("Required Field");
            uname.requestFocus();
            return;
        }
        if(emailId.isEmpty()){
            email.setError("Required Field");
            email.requestFocus();
            return;
        }
        if(password.isEmpty()){
            pass.setError("Required Field");
            pass.requestFocus();
            return;
        }
        if(password.length()<6){
            pass.setError("Password must be atleast 6 charecters long");
            pass.requestFocus();
            return;
        }

        mAuth.createUserWithEmailAndPassword(emailId,password).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if(task.isSuccessful()){
                    finish();
                    Toast.makeText(Signup.this, "User Registered", Toast.LENGTH_SHORT).show();
                    Intent intent=new Intent(Signup.this,Profile.class);

                    intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);

                    startActivity(intent);
                }
                else{
                    if(task.getException() instanceof FirebaseAuthUserCollisionException){
                        Toast.makeText(Signup.this, "User already exist", Toast.LENGTH_SHORT).show();
                    }
                }

            }
        });
    }


    @Override
    public void onClick(View v) {
        switch(v.getId()){
            case R.id.textView2:
                finish();
                startActivity(new Intent(this,MainActivity.class));
                break;
            case R.id.button3:
                registerUser();
                break;
        }
    }
}
