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

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            // Only make it transparent again if menu is not open on mobile
            if (window.innerWidth > 768) {
                navbar.classList.remove('scrolled');
            }
        }
    });

    // Check initial scroll position
    if (window.scrollY > 50 || window.innerWidth <= 768) {
        navbar.classList.add('scrolled');
    }

    window.addEventListener('resize', () => {
        if (window.innerWidth <= 768) {
            navbar.classList.add('scrolled');
        } else if (window.scrollY <= 50) {
            navbar.classList.remove('scrolled');
        }
    });


    // Active Nav Link on Scroll
    const sections = document.querySelectorAll('section, footer');

    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (scrollY >= (sectionTop - 200)) {
                current = section.getAttribute('id');
            }
        });

        navLinksItems.forEach(li => {
            li.classList.remove('active');
            if (li.getAttribute('href').includes(current)) {
                li.classList.add('active');
            }
        });
    });

    // Theme Toggle
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = themeToggleBtn.querySelector('i');

    // Check for saved user preference, if any, on load of the website
    const darkMode = localStorage.getItem('darkMode');

    if (darkMode === 'enabled') {
        document.body.classList.add('dark-mode');
        themeIcon.classList.remove('fa-mug-hot');
        themeIcon.classList.add('fa-coffee');
    }

    themeToggleBtn.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');

        if (document.body.classList.contains('dark-mode')) {
            localStorage.setItem('darkMode', 'enabled');
            themeIcon.classList.remove('fa-mug-hot');
            themeIcon.classList.add('fa-coffee');
        } else {
            localStorage.setItem('darkMode', null);
            themeIcon.classList.remove('fa-coffee');
            themeIcon.classList.add('fa-mug-hot');
        }
    });

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
window.onload=function(){
  window.scrollTo(0,0);
};
