package com.example.shuk.interfaces

import retrofit2.Call
import retrofit2.http.Field
import retrofit2.http.FormUrlEncoded
import retrofit2.http.POST

interface ApiService {
    companion object {
        const val API_SERVER_URL = "http://127.0.0.1:8000/"
    }

    @FormUrlEncoded
    @POST("/api/login")
    fun login (
        @Field("funcion") function: String,
        @Field("username") username: String,
        @Field("password") password: String) : Call<String>
}