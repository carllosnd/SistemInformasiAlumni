// Buat file navbar.js
document.addEventListener("DOMContentLoaded", function () {
    const navbarContainer = document.querySelector(".navbar-container");
    const navbarContent = `
      <div class="navbar">
      <div class="logo">
      <img src="/static/assets/img/ukrimlogo.png" alt="Logo" />
      <span>Sistem Informasi Alumni UKRIM</span>
    </div>
    <ul class="nav-list">
      <li><a href="">Beranda</a></li>
      <li class="dropdown">
        <a href="#">Tentang Kami</a>
        <ul class="dropdown-menu">
          <li><a href="visimisi/">Visi & Misi</a></li>
          <li><a href="strorg/">Struktur Organisasi</a></li>
        </ul>
      </li>
      <li class="dropdown">
        <a href="#">Alumni</a>
        <ul class="dropdown-menu">
          <li><a href="alumni/">Data Alumni</a></li>
          <li><a href="login/">Login Alumni</a></li>
        </ul>
      </li>
      <li class="dropdown">
        <a href="#">Informasi</a>
        <ul class="dropdown-menu">
          <li><a href="agenda/">Agenda</a></li>
          <li><a href="pengumuman/">Pengumuman</a></li>
          <li><a href="loker/">Lowongan Kerja (Loker)</a></li>
        </ul>
      </li>
      <li><a href="donasi">Donasi</a></li>
    </ul>
  </div>
    `;
    navbarContainer.innerHTML = navbarContent;
  });
  