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

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    EditText email = findViewById(R.id.emailId);
    EditText pass = findViewById(R.id.password);
    TextView sign = findViewById(R.id.signUp);
    Button lgin = findViewById(R.id.login);
    private FirebaseAuth mAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        sign.setOnClickListener(this);
        lgin.setOnClickListener(this);
        mAuth = FirebaseAuth.getInstance();


    }


    private void userLogin() {
        String mail = email.getText().toString();
        String password = pass.getText().toString();
        if (mail.isEmpty()) {
            email.setError("Field is required");
            email.requestFocus();
            return;
        }
        if (password.isEmpty()) {
            pass.setError("Field is required");
            pass.requestFocus();
            return;

        }
        mAuth.signInWithEmailAndPassword(mail, password).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if (task.isSuccessful()) {
                    finish();
                    Toast.makeText(MainActivity.this, "Logged in", Toast.LENGTH_SHORT).show();
                    Intent intent = new Intent(MainActivity.this, FeedActivity.class);
                    intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
                    startActivity(intent);
                }
            }
        });
    }

    @Override
    protected void onStart() {
        super.onStart();
        if(mAuth.getCurrentUser()!=null){
            finish();
            startActivity(new Intent(this,Profile.class));
        }
    }

    @Override
    public void onClick(View view) {
        switch (view.getId()) {
            case R.id.login:
                userLogin();
                break;

            case R.id.signUp:
                startActivity(new Intent(this, Signup.class));
                break;

        }
    }
}
