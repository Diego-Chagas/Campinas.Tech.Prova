import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  counter = 0;
  title = 'Busque aqui o seu imóvel!';
  buttonTitle = "Titulo do botão";
  imgSrc="https://www.rotajuridica.com.br/wp-content/uploads/2015/08/casa-pr%C3%B3pria.jpg";
  imgWidth = 300;
  valor = 10;
  buttonStyle = 'background: orange; padding: 10px; font-size: 10px';
  incrementaTilte(value){
    this.title = value;
  }

}
