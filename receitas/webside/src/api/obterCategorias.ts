import type ICategoria from '@/interfaces/ICategoria';
import axios from 'axios';
import { ref, onMounted, h } from 'vue';

export async function obterCategorias(): Promise<ICategoria[]> {
    try {
      const response = await axios.get<ICategoria[]>('http://localhost:8000/categorias/');
      return response.data;
    } catch (error) {
      console.error('Erro ao carregar receitas:', error);
      return []; // Retorna uma lista vazia em caso de erro
    }
  }