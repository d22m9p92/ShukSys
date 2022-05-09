import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ApiService } from '../../servicios/api/api.service';
import { LoginI,LoginO } from 'src/app/modelos/login.interface';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';
import { timeout } from 'rxjs';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  form: FormGroup
  loading= false; 

  constructor(private fb: FormBuilder, private api:ApiService, private router:Router, private _snackBar: MatSnackBar) {
    this.form = this.fb.group({
      usuario: ['',Validators.required],
      password: ['',Validators.required],
    })
   }

  ngOnInit(): void {
  }

  
  ingresar(form:LoginI){
    this.api.login(form).subscribe(data=>{
        let dataResponse:LoginO= data;
        if (dataResponse.status == "sucess"){
          localStorage.setItem("token", dataResponse.message);
          this.fakeLoading(dataResponse.staff);
        } else {
          this.error(dataResponse.message);
          this.form.reset();
        }
      });

  
    }
    error(mensaje:string){
      this._snackBar.open(mensaje,'',{
        duration: 3000,
        horizontalPosition: 'center',
        verticalPosition: 'bottom'
      })
    }

    fakeLoading(staff:boolean){
    this.loading = true;     
    setTimeout(() => {

      //si es staff va al admin, si no al dashboard de clientes
      if(staff== true){
      this.router.navigate(['dashboard']);
      }

    }, 1500);

    }

}