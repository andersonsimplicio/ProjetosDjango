<template>
    <header class="banner">
    <div class="apresetacao">
      <img src="../assets/image/logo.svg" alt="Logo site receitas" class="logo">
      <p class="cabecalho-lg frase-cabecalho">
        <span class="texto-verde">
          Um banquete de ideias
        </span>
        para despertar o chef em você!
      </p>
      <p class="subtitulo-lg">
        explore as receitas
      </p>
    </div>
    <img src="../assets/image/foto-banner.png" alt="" class="foto-banner">
  
  </header>
 
</template>

<style>
.banner {
    padding: 4rem 7.5rem;
    color: var(--creme);
  
    display: flex;
    justify-content: space-between;
    align-items: center;
    column-gap: 3.25rem;
  }
  
  .logo {
    height: 4.5rem;
    margin-bottom: 3rem;
  }
  
  .frase-cabecalho {
    margin-bottom: 2rem;
  }
  
  .texto-verde {
    color: var(--verde-medio, #3D6D4A);
  }
  
  .foto-banner {
    width: 35rem;
  }
  
  @media only screen and (max-width: 1300px) {
    .banner {
      padding: 4rem 3.75rem;
      flex-direction: column;
      align-items: center;
      gap: 1rem;
    }
  
    .logo {
      display: block;
      margin-left: auto;
      margin-right: auto;
    }
  }
  
  @media only screen and (max-width: 767px) {
    .banner {
      padding: 4rem 1.5rem;
    }
  
    .foto-banner {
      width: min(100%, 21.25rem);
    }
  }


</style>