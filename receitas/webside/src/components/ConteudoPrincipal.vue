<script lang="ts">
import type IngredienteIterface from '@/interfaces/IngredienteInteface';
import SelecionarIngredientes from './SelecionarIngredientes.vue';
import SuaLista from './SuaLista.vue';
import Rodape from './Rodape.vue';

export default { 
  data(){
   
    return{
      ingredientes: [] as IngredienteIterface[]
    }
  },
  components:{SelecionarIngredientes,SuaLista},
  methods:{
    adcionarIngredientes(ingrediente:string){
      this.ingredientes.push({nome:ingrediente});
      console.log("Teste");
    },
    removerIngrediente(ingrediente: string) {
      console.log("Teste");
      this.ingredientes = this.ingredientes.filter(iLista => ingrediente !== iLista.nome);
    },
  }
}
</script>

<template>
    <main class="conteudo-principal">
        <SuaLista :ingredientes="ingredientes"/>
        <SelecionarIngredientes
          @adicionar-ingrediente="adcionarIngredientes($event)"
          @remover-ingrediente="removerIngrediente($event)"
        />
    </main>
</template>

<style scoped>
.conteudo-principal {
  padding: 6.5rem 7.5rem;
  border-radius: 3.75rem 3.75rem 0rem 0rem;
  background: var(--creme, #FFFAF3);
  color: var(--cinza, #444);

  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5rem;
}

.sua-lista-texto {
  color: var(--coral, #F0633C);
  display: block;
  text-align: center;
  margin-bottom: 1.5rem;
}

@media only screen and (max-width: 1300px) {
  .conteudo-principal {
    padding: 5rem 3.75rem;
    gap: 3.5rem;
  }
}

@media only screen and (max-width: 767px) {
  .conteudo-principal {
    padding: 4rem 1.5rem;
    gap: 4rem;
  }
}
</style>

