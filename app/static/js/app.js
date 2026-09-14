/* ============================================================
   SECURE DIGITAL EVIDENCE PLATFORM — Frontend Interactions
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
    
    // --- 1. Mobile Sidebar Toggle ---
    const mobileToggle = document.getElementById('mobile-toggle');
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebar-overlay');
    
    if (mobileToggle && sidebar && overlay) {
        function toggleSidebar() {
            const isOpen = sidebar.classList.contains('open');
            if (isOpen) {
                sidebar.classList.remove('open');
                overlay.style.display = 'none';
                mobileToggle.setAttribute('aria-expanded', 'false');
            } else {
                sidebar.classList.add('open');
                overlay.style.display = 'block';
                mobileToggle.setAttribute('aria-expanded', 'true');
            }
        }
        
        mobileToggle.addEventListener('click', toggleSidebar);
        overlay.addEventListener('click', toggleSidebar);
    }

    // --- 2. Auto-dismiss Flash Toasts ---
    const toastContainer = document.getElementById('toast-container');
    if (toastContainer) {
        const toasts = toastContainer.querySelectorAll('.toast');
        toasts.forEach((toast, index) => {
            // Stagger dismissal slightly for multiple toasts
            setTimeout(() => {
                toast.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
                toast.style.opacity = '0';
                toast.style.transform = 'translateX(10px)';
                
                setTimeout(() => {
                    toast.remove();
                    if (toastContainer.children.length === 0) {
                        toastContainer.remove();
                    }
                }, 400); // Wait for fade transition
            }, 4000 + (index * 500)); // Show for 4 seconds
        });
    }

    // --- 3. Subtle Button Click Effect ---
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(btn => {
        btn.addEventListener('mousedown', function() {
            this.style.transform = 'scale(0.98)';
        });
        btn.addEventListener('mouseup', function() {
            this.style.transform = '';
        });
        btn.addEventListener('mouseleave', function() {
            this.style.transform = '';
        });
    });
});
