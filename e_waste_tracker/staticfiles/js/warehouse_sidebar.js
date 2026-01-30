window.addEventListener("DOMContentLoaded", () => {
  document
    .getElementById("toggleSidebar")
    .addEventListener("click", function () {
      const sidebar = document.getElementById("sidebar");
      const icon = document.getElementById("icon-swipe");

      // Toggle sidebar open/close
      sidebar.classList.toggle("collapsed");

      // Toggle the icon class
      if (sidebar.classList.contains("collapsed")) {
        icon.classList.remove("bi-layout-sidebar-inset");
        icon.classList.add("bi-layout-sidebar-inset-reverse");
      } else {
        icon.classList.remove("bi-layout-sidebar-inset-reverse");
        icon.classList.add("bi-layout-sidebar-inset");
      }
    });
});
