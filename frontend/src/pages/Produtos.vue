<template>
<header class="headercinza">    
    <div class="controls-header container">
        <div class="wrapper-header">
            <div class="brand-header">
                <h1 id="logotipo" class="logo"><a href="/" id="Logo">viaprodutos</a></h1>
                <small class="viavarejo" style="font-size:10px">Produtos viavarejo</small>
            </div>
            <form>
                <div class="search-control-header" id="formBusca">
                    
                    <div class="select-dropdown">
                        <select id="select" name="store" v-model="store" @change="mudarCor">
                            <option value="">Selecione a loja</option>
                            <option value="casasbahia">Casas Bahia</option>
                            <option value="extra">Extra</option>
                            <option value="pontofrio">Ponto Frio</option>
                        </select>
                    </div>
                    
                    <div class="select-dropdown">
                        <select name="resultsPerPage" v-model="resultsPerPage">
                            <option value="">Resultados por página</option>
                            <option value="5">5</option>
                            <option value="10">10</option>
                            <option value="20">20</option>
                            <option value="50">50</option>
                            <option value="100">100</option>
                            </select>
                    </div>
                
                    <label for="strBusca" id="search_label">
                        <span class="form__inputTitle">Buscar</span>
                        <input name="terms" v-model="terms" id="strBusca" type="text" placeholder="Buscar os melhores produtos" class="input-search-header" onkeydown="return (event.keyCode!=13);">
                        
                    </label>
                    <button type="button" @click="listarProdutos" id="btnOK" class="button-search-header" aria-label="Buscar"><!--type="submit"-->
                            <span style="margin-top:10px;padding:30px;color:white"><p>OK</p></span>
                    </button>
                    
                </div>
            </form>
        </div>
    </div>
</header>


<section class="cards">
  <article class="card" v-for="produto in produtos" :key="produto.name">
    <a :href="produto.url" target="_blank" rel="noopener noreferrer">
    <picture class="thumbnail">
         <img class="category__01" :src="produto.images" alt="" />
    </picture>
    <div class="card-content">
      <p class="category category__01">R$ {{produto.preco_desconto}}</p>
      <p style="text-align:center">{{ produto.name }}</p>
      
   </div>
    
    <footer>
      <div class="post-meta">
        <i style="color: #50c6db" class="fa fa-credit-card"></i>
        <span style="color:#50c6db" class="timestamp">{{ produto.preco_cartao }}</span>
        <span class="marca">{{produto.marca}} </span>
        </div>
    </footer>
    </a>
  </article>
</section>

</template>

<script>
import api from '@/services/api.js'
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Produtos',
  data(){
    return {
        resultsPerPage: 10,
        terms: '',
        produtos: [],
        store: ''
    }
  },
  methods: {
    async listarProdutos() {
      await api.get('/api/?&resultsPerPage='+ this.resultsPerPage + '&terms=' + this.terms + '&store=' + this.store)
      .then(response => {
          this.produtos = response.data
      })
      document.querySelector('.tecno').remove()
    },
    mudarCor(){
        var seletor = document.getElementById("select").value
        if (seletor == 'casasbahia'){
            //document.querySelector(".headercinza").style.backgroundColor = 'rgb(247, 247, 247)'
            //document.querySelector("#Logo").style.color = 'blue'
            document.querySelector(".button-search-header").style.backgroundColor = 'rgb(0, 51, 198)'
        }else if(seletor == 'extra'){
             //document.querySelector(".headercinza").style.backgroundColor = 'rgb(193, 25, 38)'
             //document.querySelector("#Logo").style.color = 'white'
             document.querySelector(".button-search-header").style.backgroundColor = 'rgb(193, 25, 38)'

        }else if(seletor == 'pontofrio'){
             //document.querySelector(".headercinza").style.backgroundColor = 'rgb(33, 33, 33)'
             //document.querySelector("#Logo").style.color = 'white'
             document.querySelector(".button-search-header").style.backgroundColor = 'rgb(255, 94, 0)'
        }
    }
  }
}
</script>

<style>
header{
    background-color: #f1f1f1;;
    display: block;
    color: rgb(10, 10, 10);
  }

  .controls-header {
    padding: 0 0 20px 0;
  }

  .wrapper-header {
    width: 1280px;
    margin: 0 auto;
      display: flex;
  }

  .brand-header{
    padding-top: 22px;
  }

  #formBusca {
    display: flex;
    align-items: center;
  }

  .search-control-header {
    display: block;
    position: relative;
    padding: 0;
    margin: 0 0 0 100px;
  }
  
  #search_label {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 80px;
    min-width: 80px;
  } 

  .input-search-header {
    width: 380px;
    /*background: url('https://cdn.icon-icons.com/icons2/1111/PNG/128/loupe_79257.png') no-repeat 12px 13px #fff;*/
    width: 447px;
    height: 49px;
    border-radius: 60px 0 0 60px;
    border: 0;
    padding: 0 0 0 47px;
    margin: 0;
    color: #666666;
    font-size: 14px;
    font-family: "Sarabun",Tahoma,Verdana,Segoe,sans-serif;
    float: left;
  }

  .form__inputTitle {
    width: 65px;
    height: 49px;
    font-weight: 700;
    font-size: 0px;
    color: #404040;
    line-height: 22px;
    padding-left: 4px;
    border-radius: 60px 0 0 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
  }

  #btnOK {
    text-indent: 0;
  }

  .button-search-header {
    background: rgb(10, 152, 105);;
    height: 49px;
    border: 0;
    border-radius: 0 60px 60px 0;
    float: left;
    text-align: center;
    cursor: pointer;
    outline: 0;
  }

span {
    font-family: "Sarabun",Tahoma,Verdana,Segoe,sans-serif;
    font-size: 10px;
    padding: 3px;
    font-weight: 700;
}

.select-dropdown,
.select-dropdown * {
    margin: 0;
    padding: 0;
    position: relative;
    box-sizing: border-box;
}
.select-dropdown {
    position: relative;
    background-color: #E6E6E6;
    border-radius: 4px;
    margin-left: 20px;
}
.select-dropdown select {
    font-size: 1rem;
    font-weight: normal;
    max-width: 100%;
    padding: 8px 24px 8px 10px;
    border: none;
    background-color: transparent;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
}
.select-dropdown select:active, .select-dropdown select:focus {
    outline: none;
    box-shadow: none;
}
.select-dropdown:after {
    content: "";
    position: absolute;
    top: 50%;
    right: 8px;
    width: 0;
    height: 0;
    margin-top: -2px;
    border-top: 5px solid #aaa;
    border-right: 5px solid transparent;
    border-left: 5px solid transparent;
}


.cards {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); /* see notes below */
    grid-auto-rows: minmax(200px, auto);
    grid-gap: 1rem;
}

.card {
  /*height: 200px;*/
  /*background: red;*/
    border: 1px solid #e7e7e7;
    border-radius: 4px;
    padding: .5rem;
    -webkit-box-shadow: 0 2px 2px rgba(0, 0, 0, 0.15);
    box-shadow: 0 2px 2px rgba(0, 0, 0, 0.15);
    display: flex;
  /* -webkit-box-orient: vertical; */
  /* -webkit-box-direction: normal; */
    -ms-flex-direction: column;
    flex-direction: column;
    position: relative;
    color: #5d5e5e;
} /* li item */

.thumbnail img {
    fill: #c7c4c4;
    height: 200px;
    padding-left: 5px;
    background-color: white;
}

.card-content {
    font-size: .80rem;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;
}

.panel.card-panel .panel-header {
    background-color: #ffffff;
    font-size: .75rem;
    font-weight: 400;
    height: 25px !important;
}

.panel.card-panel .panel-content {
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;
}

.category {
    font-size: .75rem;
    text-transform: uppercase;
}

footer {
    border-top: 2px solid #e7e7e7;
    margin: .5rem 0 0;
    min-height: 30px;
    font-size: .5rem;
}

.category {
    position: absolute;
    top: 0px;
    left: 0;
    color: #fff;
    
    padding: 10px 15px;
    font-size: 14px;
    font-weight: 600;
    text-transform: uppercase;
}

.category__01 {
    background-color: #50c6db;
}


.post-meta {
    margin-top: .5rem;
    margin-left: 3px;
}

.marca {
    margin-left: .8rem;
}

</style>