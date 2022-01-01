package com.example.javasocketapp;

import static com.example.javasocketapp.R.id.button;
import static com.example.javasocketapp.R.id.button2;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import java.io.*;
import java.net.*;
import java.lang.*;

public class MainActivity<policy> extends AppCompatActivity {

    private Button mButton;
    private Button stopButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mButton = findViewById(button);
        mButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
            {
                Thread thread = new Thread(new Runnable() {

                    @Override
                    public void run() {
                        try  {
                            Socket socket=new Socket("192.168.10.4",12345);
                            DataInputStream input = new DataInputStream(System.in);
                            DataOutputStream out = new DataOutputStream(socket.getOutputStream());
                            try
                            {
                                out.writeUTF("START");
                            }
                            catch(IOException i)
                            {
                                System.out.println(i);
                            }
                            socket.close();
                        } catch (Exception e) {
                            e.printStackTrace();
                        }
                    }
                });
                thread.start();
            }
        });

        stopButton = findViewById(button2);
        stopButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view)
            {
                Thread thread = new Thread(new Runnable() {

                    @Override
                    public void run() {
                        try  {
                            Socket socket1=new Socket("192.168.10.4",12345);
                            DataInputStream input1 = new DataInputStream(System.in);
                            DataOutputStream out1 = new DataOutputStream(socket1.getOutputStream());
                            try
                            {
                                String line="STOP";
                                out1.writeUTF(line);
                            }
                            catch(IOException i)
                            {
                                System.out.println(i);
                            }

                            socket1.close();
                        } catch (Exception e) {
                            e.printStackTrace();
                        }
                    }
                });
                thread.start();
            }
        });

    }
}