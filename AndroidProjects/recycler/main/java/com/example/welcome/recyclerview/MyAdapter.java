package com.example.welcome.recyclerview;

import android.content.Context;
import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import com.bumptech.glide.Glide;

class MyAdapter extends RecyclerView.Adapter <MyAdapter.MyViewHolder> {
private  Context context;
    Users[] data;
    public MyAdapter(Context context, Users[] data){

        this.context=context;
        this.data=data;

    }
    @NonNull
    @Override
    public MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater inflater=LayoutInflater.from(parent.getContext());
        View view=inflater.inflate(R.layout.list_item_layout,parent,false);
        return new MyViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull MyViewHolder holder, int position) {
        String title=data[position].toString();
        Users user=data[position];
        holder.title.setText(title);
        Glide.with(holder.icon.getContext()).load(user.getImageUrl()).into(holder.icon);//get url from the json using method

    }

    @Override
    public int getItemCount() {
        return data.length ;
    }

    public class MyViewHolder extends RecyclerView.ViewHolder{

        ImageView icon;
        TextView title;
        public MyViewHolder(View itemView) {
            super(itemView);
            icon=itemView.findViewById(R.id.icon);
            title=itemView.findViewById(R.id.title);
        }
    }

}
