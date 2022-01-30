package com.example.shuk.activity

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.Toast
import com.example.shuk.R
import com.example.shuk.interfaces.ApiService
import com.example.shuk.models.Login
import com.google.android.material.textfield.TextInputEditText
import retrofit2.Retrofit
import retrofit2.converter.scalars.ScalarsConverterFactory


class LoginActivity : AppCompatActivity() {
    private lateinit var retrofit: Retrofit
    private lateinit var service: ApiService
    private lateinit var login: Login
    private var username: String = ""
    private var password: String = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        service = createApiService()
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        val usernameInput = findViewById<TextInputEditText>(R.id.username)
        val passwordInput = findViewById<TextInputEditText>(R.id.password)
        val ingresarButton = findViewById<Button>(R.id.ingresar)

        ingresarButton.setOnClickListener{
            username = usernameInput.text.toString().trim()
            password = passwordInput.text.toString().trim()

            if (username.isNotEmpty()){
                if(password.isNotEmpty()){
                    executeLogin(username,password)
                }else{
                    Toast.makeText(this,"Contraseña requerida",Toast.LENGTH_SHORT).show()
                }
            }else{
                Toast.makeText(this,"Email requerido",Toast.LENGTH_SHORT).show()
            }
        }
    }

    private fun createApiService(): ApiService {
        retrofit = Retrofit.Builder()
            .baseUrl(ApiService.API_SERVER_URL)
            .addConverterFactory(ScalarsConverterFactory.create())
            .build()
        return retrofit.create(ApiService::class.java)
    }

    private fun executeLogin(username: String, password: String){
        val call = service.login("login",username,password)

        //https://www.digitaldot.es/como-implementar-log-in-en-kotlin-con-retrofit/
    }

}


