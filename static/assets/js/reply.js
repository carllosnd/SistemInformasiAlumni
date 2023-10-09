document.addEventListener("DOMContentLoaded", function() {
    // Mengaktifkan tampilan form reply saat tombol "Reply" diklik
    const replyButtons = document.querySelectorAll(".reply-button");
    replyButtons.forEach(button => {
       button.addEventListener("click", function(event) {
          event.preventDefault();
          const replyForm = this.nextElementSibling;
          replyForm.style.display = "block";
       });
    });
});