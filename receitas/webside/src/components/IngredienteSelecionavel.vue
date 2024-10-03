<script lang="ts">
import Tag from "./Tag.vue";

export default {
  props: {
    ingrediente:{type:String , required:true}
  },
  components:{Tag},
  data(){
    return {
        selecionado:false
    }
  },
  methods:{
    aoClicar(){
      this.selecionado = !this.selecionado
      if(this.selecionado){
        this.$emit('adicionarIngrediente',this.ingrediente)
      }else{
        this.$emit('removerIngrediente',this.ingrediente)
      }
    }
  },
  emits:['adicionarIngrediente','removerIngrediente']
}
</script>
<template >
    <!--outra forma de user é [@click="selecionado = !selecionado] para escutar eventos do DOM" -->
   <button
     class="ingrediente"
     v-on:click="aoClicar" 
     :aria-pressed="selecionado"
   > <Tag :texto="ingrediente" :ativa="selecionado"/></button>
</template>


<style scoped>
.ingrediente{
    cursor: pointer;
}
</style>