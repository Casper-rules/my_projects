package com.example.welcome.recyclerview;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.widget.Adapter;
import android.widget.Toast;

import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class MainActivity extends AppCompatActivity {
    public static final String Url = "";//the url for the videos
Users[] myData;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        RecyclerView programmingList=findViewById(R.id.programmingList);
        programmingList.setLayoutManager(new LinearLayoutManager(this));
        programmingList.setAdapter(new MyAdapter(this,myData));
        StringRequest request=new StringRequest(Url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                Log.d("Class",response);
                GsonBuilder gsonBuilder=new GsonBuilder();
                Gson gson=gsonBuilder.create();
                Users[] users= gson.fromJson(response,Users[].class);
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Toast.makeText(MainActivity.this, "Something went wrong", Toast.LENGTH_SHORT).show();
            }
        });
        RequestQueue queue=Volley.newRequestQueue(this);
        queue.add(request);
    }
}
//receive java object from json and copy the classes in the project to be used
