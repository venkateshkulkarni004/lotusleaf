(() => {
  const hotels = [
    ["Ardena Hotels", "ArdenaHotels.html"],
    ["LotusLeaf Hotels", "Portfolio.html"],
    ["LotusLeaf Resorts", "Portfolio.html"]
  ];

  const createHotelsList = (className, iconClass = "") => {
    const list = document.createElement("ul");
    list.className = className;
    hotels.forEach(([label, href]) => {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = href;
      link.textContent = label;
      if (iconClass) {
        const icon = document.createElement("i");
        icon.className = iconClass;
        icon.setAttribute("aria-hidden", "true");
        link.append(" ", icon);
      }
      item.append(link);
      list.append(item);
    });
    return list;
  };

  const navList = document.querySelector("#navMenu .navbar-nav");
  const collectionToggle = document.getElementById("ourHotelsBtn");
  if (navList && collectionToggle && !document.getElementById("ourBrandsBtn")) {
    const item = document.createElement("li");
    item.className = "nav-item dropdown";

    const toggle = document.createElement("a");
    toggle.className = "nav-link dropdown-toggle";
    toggle.href = "javascript:void(0)";
    toggle.id = "ourBrandsBtn";
    toggle.setAttribute("role", "button");
    toggle.setAttribute("data-bs-toggle", "dropdown");
    toggle.setAttribute("aria-expanded", "false");
    toggle.textContent = "Our Brands";

    const menu = document.createElement("ul");
    menu.className = "dropdown-menu dropdown-menu-end hotel-dropdown";
    menu.setAttribute("aria-labelledby", "ourBrandsBtn");
    hotels.forEach(([label, href]) => {
      const entry = document.createElement("li");
      const link = document.createElement("a");
      link.className = "dropdown-item";
      link.href = href;
      link.textContent = label;
      entry.append(link);
      menu.append(entry);
    });

    item.append(toggle, menu);
    navList.insertBefore(item, collectionToggle.closest(".nav-item"));
  }

  const sideMenu = document.getElementById("rightSideMenu");
  const sideList = sideMenu?.querySelector("ul.side-menu, ul.list-group");
  if (!sideList || sideMenu.querySelector("[data-our-hotels-slide]")) return;

  if (sideList.classList.contains("side-menu")) {
    const item = document.createElement("li");
    item.dataset.ourHotelsSlide = "true";

    const toggle = document.createElement("a");
    toggle.href = "javascript:void(0)";
    toggle.setAttribute("aria-expanded", "false");
    toggle.innerHTML = '<span>Our Brands</span><i class="bi bi-chevron-down" aria-hidden="true"></i>';

    const submenu = createHotelsList("side-about-menu");
    submenu.style.display = "none";
    item.append(toggle, submenu);
    const collectionItem = Array.from(sideList.children).find((entry) =>
      entry.textContent.includes("Our Collection")
    );
    sideList.insertBefore(item, collectionItem || null);

    toggle.addEventListener("click", (event) => {
      event.preventDefault();
      const isOpen = submenu.style.display !== "block";
      submenu.style.display = isOpen ? "block" : "none";
      toggle.setAttribute("aria-expanded", String(isOpen));
      toggle.querySelector("i").className = isOpen ? "bi bi-chevron-up" : "bi bi-chevron-down";
    });
  } else {
    const item = document.createElement("li");
    item.className = "list-group-item";
    item.dataset.ourHotelsSlide = "true";

    const heading = document.createElement("strong");
    heading.className = "d-block mb-2";
    heading.textContent = "Our Brands";
    item.append(heading, createHotelsList("list-unstyled d-flex flex-column gap-2 ps-3"));

    const collectionItem = Array.from(sideList.children).find((entry) =>
      entry.textContent.includes("Our Collection")
    );
    sideList.insertBefore(item, collectionItem || null);
  }
})();
