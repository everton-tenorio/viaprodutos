<template>
  <Produtos />
  <Home />
</template>

<script>
import './styles/global.css'
import Home from './components/Home'
import Produtos from './pages/Produtos'
export default {
  name: 'App',
  components:{
    Produtos,
    Home
}
}
</script>