document.addEventListener('DOMContentLoaded', () => {
    // Mobile Navigation Toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const navLinksItems = document.querySelectorAll('.nav-links a');

    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        const icon = hamburger.querySelector('i');
        if (navLinks.classList.contains('active')) {
            icon.classList.remove('fa-bars');
            icon.classList.add('fa-xmark');
        } else {
            icon.classList.remove('fa-xmark');
            icon.classList.add('fa-bars');
        }
    });

    // Close mobile menu when a link is clicked
    navLinksItems.forEach(item => {
        item.addEventListener('click', () => {
            navLinks.classList.remove('active');
            const icon = hamburger.querySelector('i');
            icon.classList.remove('fa-xmark');
            icon.classList.add('fa-bars');
        });
    });

    // Navbar Scroll Effect
    const navbar = document.getElementById('navbar');
    let isScrollTicking = false;

    window.addEventListener('scroll', () => {
        if (!isScrollTicking) {
            // DOM Read phase (outside of animation frame)
            const currentScrollY = window.scrollY;
            const currentWidth = window.innerWidth;

            window.requestAnimationFrame(() => {
                // DOM Write phase
                if (currentScrollY > 50) {
                    navbar.classList.add('scrolled');
                } else {
                    // Only make it transparent again if menu is not open on mobile
                    if (currentWidth > 768) {
                        navbar.classList.remove('scrolled');
                    }
                }
                isScrollTicking = false;
            });
            isScrollTicking = true;
        }
    }, { passive: true });

    // Check initial scroll position
    window.requestAnimationFrame(() => {
        if (window.scrollY > 50 || window.innerWidth <= 768) {
            navbar.classList.add('scrolled');
        }
    });

    let isResizeTicking = false;
    window.addEventListener('resize', () => {
        if (!isResizeTicking) {
            // DOM Read phase (outside of animation frame)
            const currentWidth = window.innerWidth;
            const currentScrollY = window.scrollY;

            window.requestAnimationFrame(() => {
                // DOM Write phase
                if (currentWidth <= 768) {
                    navbar.classList.add('scrolled');
                } else if (currentScrollY <= 50) {
                    navbar.classList.remove('scrolled');
                }
                isResizeTicking = false;
            });
            isResizeTicking = true;
        }
    }, { passive: true });


    // Active Nav Link on Scroll (Optimized with Intersection Observer)
    const sections = document.querySelectorAll('section, footer');
    const observerOptions = {
        root: null,
        rootMargin: '-50% 0px -50% 0px',
        threshold: 0
    };

    const navObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const currentId = entry.target.getAttribute('id');
                navLinksItems.forEach(li => {
                    li.classList.remove('active');
                    if (li.getAttribute('href').includes(currentId)) {
                        li.classList.add('active');
                    }
                });
            }
        });
    }, observerOptions);

    sections.forEach(section => navObserver.observe(section));

    // Theme Toggle
    const themeToggleBtn = document.getElementById('theme-toggle');
    const svgMugHot = '<svg height="1em" width="1em" style="vertical-align: -0.125em; fill: currentColor;" viewBox="0 0 512 512"><path d="M127.1 146.5c1.3 7.7 8 13.5 16 13.5h16.5c9.8 0 17.6-8.5 16.3-18-3.8-28.2-16.4-54.2-36.6-74.7-14.4-14.7-23.6-33.3-26.4-53.5C111.8 5.9 105 0 96.8 0H80.4C70.6 0 63 8.5 64.1 18c3.9 31.9 18 61.3 40.6 84.4 12 12.2 19.7 27.5 22.4 44.1zm112 0c1.3 7.7 8 13.5 16 13.5h16.5c9.8 0 17.6-8.5 16.3-18-3.8-28.2-16.4-54.2-36.6-74.7-14.4-14.7-23.6-33.3-26.4-53.5C223.8 5.9 217 0 208.8 0h-16.4c-9.8 0-17.5 8.5-16.3 18 3.9 31.9 18 61.3 40.6 84.4 12 12.2 19.7 27.5 22.4 44.1zM400 192H32c-17.7 0-32 14.3-32 32v192c0 53 43 96 96 96h192c53 0 96-43 96-96h16c61.8 0 112-50.2 112-112s-50.2-112-112-112zm0 160h-16v-96h16c26.5 0 48 21.5 48 48s-21.5 48-48 48z"/></svg>';
    const svgCoffee = '<svg height="1em" width="1em" style="vertical-align: -0.125em; fill: currentColor;" viewBox="0 0 640 512"><path d="M192 384l192 0c53 0 96-43 96-96l32 0c70.6 0 128-57.4 128-128S582.6 32 512 32L120 32C106.7 32 96 42.7 96 56l0 232c0 53 43 96 96 96zM512 96c35.3 0 64 28.7 64 64s-28.7 64-64 64l-32 0 0-128 32 0zM0 464c0 26.5 21.5 48 48 48l544 0c26.5 0 48-21.5 48-48s-21.5-48-48-48L48 416c-26.5 0-48 21.5-48 48z"/></svg>';

    // Check for saved user preference, if any, on load of the website
    const darkMode = localStorage.getItem('darkMode');

    if (darkMode === 'enabled') {
        document.body.classList.add('dark-mode');
        if (themeToggleBtn) {
            themeToggleBtn.innerHTML = svgCoffee;
        }
    } else {
        if (themeToggleBtn && !themeToggleBtn.innerHTML.includes('<svg')) {
            themeToggleBtn.innerHTML = svgMugHot;
        }
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode');

            if (document.body.classList.contains('dark-mode')) {
                localStorage.setItem('darkMode', 'enabled');
                themeToggleBtn.innerHTML = svgCoffee;
            } else {
                localStorage.setItem('darkMode', null);
                themeToggleBtn.innerHTML = svgMugHot;
            }
        });
    }

    // Franchise Enquiry Modal Logic
    const franchiseModal = document.getElementById('franchise-modal');
    const openFranchiseBtn = document.getElementById('open-franchise-modal');
    const closeFranchiseBtn = document.getElementById('close-franchise-modal');
    const franchiseForm = document.getElementById('franchise-form');

    if (openFranchiseBtn && franchiseModal && closeFranchiseBtn) {
        // Open modal
        openFranchiseBtn.addEventListener('click', (e) => {
            e.preventDefault();
            franchiseModal.style.display = 'flex';
        });

        // Close modal
        closeFranchiseBtn.addEventListener('click', () => {
            franchiseModal.style.display = 'none';
        });

        // Close modal when clicking outside of it
        window.addEventListener('click', (e) => {
            if (e.target === franchiseModal) {
                franchiseModal.style.display = 'none';
            }
        });
    }

    // Handle Franchise Form Submission to WhatsApp
    if (franchiseForm) {
        franchiseForm.addEventListener('submit', (e) => {
            e.preventDefault();

            // Get form values
            const name = document.getElementById('f-name').value;
            const mobile = document.getElementById('f-mobile').value;
            const location = document.getElementById('f-location').value;
            const purpose = document.getElementById('f-purpose').value;

            // Construct WhatsApp Message
            const ownerPhone = "919021210564"; // formatting with country code +91
            const message = `*New Franchise Enquiry* 🏢\n\n*Name:* ${name}\n*Mobile:* ${mobile}\n*Location:* ${location}\n*Purpose:* ${purpose}\n\n_Sent from Shree Ram Vadapav Website_`;

            // Encode for URL
            const encodedMessage = encodeURIComponent(message);
            const whatsappUrl = `https://wa.me/${ownerPhone}?text=${encodedMessage}`;

            // Open in new tab
            window.open(whatsappUrl, '_blank');

            // Optional: Close modal and reset form
            franchiseModal.style.display = 'none';
            franchiseForm.reset();
        });
    }
});
window.onload = function () {
    window.requestAnimationFrame(() => {
        window.scrollTo(0, 0);
    });
};
