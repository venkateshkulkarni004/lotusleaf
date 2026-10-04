(() => {
  if (!document.getElementById("plain-slide-menu-styles")) {
    const styles = document.createElement("style");
    styles.id = "plain-slide-menu-styles";
    styles.textContent = `
      #rightSideMenu ul,
      #rightSideMenu ol,
      #rightSideMenu li {
        list-style: none !important;
      }
      #rightSideMenu li {
        border-top: 0 !important;
        border-bottom: 0 !important;
      }
      #rightSideMenu a,
      #rightSideMenu strong,
      #rightSideMenu b {
        font-weight: 400 !important;
        text-decoration: none !important;
      }
    `;
    document.head.append(styles);
  }

  const hotels = [
    ["Ardena Hotels", "ArdenaHotels.html"],
    ["LotusLeaf Hotels", "Portfolio.html"],
    ["LotusLeaf Resorts", "Portfolio.html"]
  ];
  const createHotelsList = (className, iconClass = "", hotelList = hotels) => {
    const list = document.createElement("ul");
    list.className = className;
    list.style.listStyle = "none";
    list.style.padding = "0";
    list.style.margin = "0";
    hotelList.forEach(([label, href]) => {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = href;
      link.textContent = label;
      link.style.display = "block";
      link.style.fontWeight = "400";
      link.style.textDecoration = "none";
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

  const footerLinks = [
    ["Our Brands", "ArdenaHotels.html"],
    ["Case Studies", "Case-Studies.html"],
    ["Success Stories", "Success-Stories.html"],
    ["Transformations", "Transformations.html"],
    ["Client Testimonials", "Client-Testimonials.html"]
  ];
  const footerLinkList = document.querySelector("footer .footer-explore .d-flex");
  if (footerLinkList) {
    footerLinks.forEach(([label, href]) => {
      const existingLink = Array.from(footerLinkList.querySelectorAll("a")).find(
        (link) => link.textContent.trim() === label
      );
      if (existingLink) {
        existingLink.href = href;
        return;
      }

      const link = document.createElement("a");
      link.className = "footer-link";
      link.href = href;
      link.textContent = label;
      const insightsLink = Array.from(footerLinkList.querySelectorAll("a")).find(
        (item) => item.getAttribute("href") === "Insights.html"
      );
      footerLinkList.insertBefore(link, insightsLink || null);
    });
  }

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
    item.style.borderBottom = "0";

    const toggle = document.createElement("a");
    toggle.href = "javascript:void(0)";
    toggle.setAttribute("aria-expanded", "false");
    toggle.innerHTML = '<span>Our Brands</span><i class="bi bi-chevron-down" aria-hidden="true"></i>';

    const submenu = createHotelsList("side-about-menu");
    submenu.style.display = "none";
    submenu.style.paddingLeft = "12px";
    submenu.querySelectorAll("li").forEach((entry) => {
      entry.style.border = "0";
    });
    submenu.querySelectorAll("a").forEach((link) => {
      link.style.padding = "8px 5px";
      link.style.fontWeight = "400";
    });
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
    item.style.border = "0";
    item.style.padding = "0";

    const heading = document.createElement("a");
    heading.href = "javascript:void(0)";
    heading.className = "d-flex align-items-center justify-content-between";
    heading.setAttribute("aria-expanded", "false");
    heading.innerHTML = '<span>Our Brands</span><i class="bi bi-chevron-down" aria-hidden="true"></i>';

    const submenu = createHotelsList("list-unstyled d-flex flex-column gap-2 ps-3");
    submenu.style.display = "none";
    item.append(heading, submenu);
    heading.addEventListener("click", (event) => {
      event.preventDefault();
      const isOpen = submenu.style.display !== "block";
      submenu.style.display = isOpen ? "block" : "none";
      heading.setAttribute("aria-expanded", String(isOpen));
      heading.querySelector("i").className = isOpen ? "bi bi-chevron-up" : "bi bi-chevron-down";
    });

    const collectionItem = Array.from(sideList.children).find((entry) =>
      entry.textContent.includes("Our Collection")
    );
    sideList.insertBefore(item, collectionItem || null);
  }
})();
