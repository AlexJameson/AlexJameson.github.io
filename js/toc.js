document.addEventListener('DOMContentLoaded', () => {
    // TOC toggle functionality
    const tocTitle = document.querySelector('.toc-title');
    const tocList = document.querySelector('.toc-list');

    if (tocTitle && tocList) {
        const toggleToC = () => {
            const isExpanded = tocList.style.display === 'block' || window.getComputedStyle(tocList).display === 'block';
            tocList.style.display = isExpanded ? 'none' : 'block';
            tocTitle.classList.toggle('expanded', !isExpanded);
        };

        tocTitle.addEventListener('click', toggleToC);
    }

    // Smooth scrolling for TOC links
    const tocLinks = document.querySelectorAll('.toc-list a[href^="#"]');
    
    tocLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            
            const targetId = link.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                // Calculate offset for fixed header
                const header = document.querySelector('.header');
                const headerHeight = header ? header.offsetHeight : 0;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerHeight - 20;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });

                // Update active TOC link
                updateActiveTocLink(link);
            }
        });
    });

    // Update active TOC link on scroll
    function updateActiveTocLink(activeLink) {
        // Remove active class from all TOC links
        document.querySelectorAll('.toc-list a').forEach(link => {
            link.classList.remove('active');
        });
        
        // Add active class to clicked link
        if (activeLink) {
            activeLink.classList.add('active');
        }
    }

    // Auto-update active TOC link based on scroll position
    function handleScroll() {
        const sections = document.querySelectorAll('section[id]');
        const scrollPosition = window.scrollY + 100;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                const activeLink = document.querySelector(`.toc-list a[href="#${sectionId}"]`);
                if (activeLink) {
                    updateActiveTocLink(activeLink);
                }
            }
        });
    }

    // Throttle scroll events for performance
    let scrollTimeout;
    window.addEventListener('scroll', () => {
        if (scrollTimeout) {
            window.cancelAnimationFrame(scrollTimeout);
        }
        scrollTimeout = window.requestAnimationFrame(handleScroll);
    });

    // Initial check for active section
    handleScroll();
});

