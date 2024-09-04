<script lang="ts">
import { onMounted, ref } from 'vue';
import { obterCategorias } from '@/api/obterCategorias';
import type ICategoria from '@/interfaces/ICategoria';
import CardCategoria from './CardCategoria.vue';


export default {
    data(){
      const categorias = ref<ICategoria[]>([]);
    onMounted(async () => {    
      categorias.value = await obterCategorias();
    });

    return {
      categorias,
    };
  },
  components:{CardCategoria},
  emits:['adicionarIngrediente']
}
</script>


<template>
    <sectio class="selecionar-ingredientes">
      <h1 class="cabecalho titulo-ingredientes">Ingredientes</h1>
      <p class="paragrago-lg instrucoes">
        Selecione os ingredientes que deseja.
      </p>
      <ul class="categorias">
        <li v-for="categoria in categorias" :key="categoria.nome">
            <CardCategoria :categoria="categoria" 
            @adicionarIngrediente="$emit('adicionarIngrediente',$event)"
            />
        </li>
      </ul>
      <p class="paragrafo dica"> 
        * presta atenção na receita
      </p>
    </sectio>
</template>

<style scoped>

.selecionar-ingredientes {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.titulo-ingredientes {
  color: var(--verde-medio, #3D6D4A);
  display: block;
  margin-bottom: 1.5rem;
}

.instrucoes {
  margin-bottom: 2rem;
}

.categorias {
  margin-bottom: 1rem;
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.dica {
  align-self: flex-start;
  margin-bottom: 3.5rem;
}

@media only screen and (max-width: 767px) {
  .dica {
    margin-bottom: 2.5rem;
  }
}
</style>