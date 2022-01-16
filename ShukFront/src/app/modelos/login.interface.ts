export interface LoginI{
    usuario:string;
    password:string;
}

export interface LoginO{
    status:string
    message:string;
    staff: boolean;
};