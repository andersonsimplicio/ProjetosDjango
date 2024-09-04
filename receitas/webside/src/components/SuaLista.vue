<script lang="ts">
import { ref, onMounted, h } from 'vue';
import SelecionarIngredientes from './SelecionarIngredientes.vue';
import type IngredienteIterface from '@/interfaces/IngredienteInteface';
import Tag from './Tag.vue';

    export default{
        props: {
            ingredientes: {
                type: Array as () => IngredienteIterface[], // Define o tipo da prop como uma lista de IngredienteIterface
                required: true // Define a prop como obrigatória
                }
        },
        data(){
            return {
            }
        }      
        ,
        components:{SelecionarIngredientes,Tag},
    }
</script>
<template>
        <section>
            <span class="subtitulo-lg sua-lista-texto">
                sua lista
            </span>
            <ul v-if="ingredientes.length" class="ingredientes-sua-lista">
                <li v-for="ingrediente in ingredientes" :key="ingrediente.nome">
                  <Tag :texto="ingrediente.nome" ativa />  
                </li>
            </ul>
            <p v-else="ingredientes.length" class="paragrafo lista-vazia">
                <img src="../assets/icones/lista-vazia.svg" alt="" class="src">
                Não lista de ingredientes
            </p>
        </section>  

</template>
<style scoped>

.ingredientes-sua-lista {
  display: flex;
  justify-content: center;
  gap: 1rem 1.5rem;
  flex-wrap: wrap;
}
.lista-vazia {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.25rem;

  color: var(--coral, #F0633C);
  text-align: center;
}



</style>