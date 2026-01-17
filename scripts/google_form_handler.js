/**
 * Google Form Handler for Chaues Productions Landing Page
 * 
 * This script provides two options for handling the contact form:
 * 1. Open Google Form in a modal overlay (embedded)
 * 2. Open Google Form in a new tab with tracking
 */

// Configuration
const GOOGLE_FORM_CONFIG = {
    // Replace this with your actual Google Form URL
    formUrl: 'https://forms.gle/YOUR_FORM_ID_HERE',

    // Options
    openInModal: false,  // Set to true to embed in modal, false to open in new tab
    trackClicks: true,   // Track form opens (requires analytics)
};

/**
 * Initialize the contact button handler
 */
document.addEventListener('DOMContentLoaded', function () {
    const contactBtn = document.querySelector('.contact-btn');

    if (!contactBtn) {
        console.error('Contact button not found');
        return;
    }

    // Add click handler
    contactBtn.addEventListener('click', handleContactClick);
});

/**
 * Handle contact button click
 */
function handleContactClick(e) {
    e.preventDefault();

    // Track the click if analytics is available
    if (GOOGLE_FORM_CONFIG.trackClicks && typeof gtag !== 'undefined') {
        gtag('event', 'contact_form_open', {
            'event_category': 'engagement',
            'event_label': 'Google Form'
        });
    }

    if (GOOGLE_FORM_CONFIG.openInModal) {
        openFormModal();
    } else {
        openFormNewTab();
    }
}

/**
 * Open form in a new tab
 */
function openFormNewTab() {
    window.open(GOOGLE_FORM_CONFIG.formUrl, '_blank', 'noopener,noreferrer');
}

/**
 * Open form in a modal overlay
 */
function openFormModal() {
    // Create modal overlay
    const modal = document.createElement('div');
    modal.className = 'form-modal';
    modal.innerHTML = `
        <div class="form-modal-overlay"></div>
        <div class="form-modal-content">
            <button class="form-modal-close" aria-label="Close form">&times;</button>
            <iframe 
                src="${GOOGLE_FORM_CONFIG.formUrl}?embedded=true" 
                frameborder="0" 
                marginheight="0" 
                marginwidth="0"
                class="form-iframe"
                title="Contact Form">
                Loading…
            </iframe>
        </div>
    `;

    // Add to page
    document.body.appendChild(modal);
    document.body.style.overflow = 'hidden';

    // Close handlers
    const closeBtn = modal.querySelector('.form-modal-close');
    const overlay = modal.querySelector('.form-modal-overlay');

    function closeModal() {
        modal.remove();
        document.body.style.overflow = '';
    }

    closeBtn.addEventListener('click', closeModal);
    overlay.addEventListener('click', closeModal);

    // Close on ESC key
    document.addEventListener('keydown', function escHandler(e) {
        if (e.key === 'Escape') {
            closeModal();
            document.removeEventListener('keydown', escHandler);
        }
    });
}

/**
 * Add required CSS for modal (if using modal option)
 * This will be injected into the page when the script loads
 */
function injectModalStyles() {
    if (!GOOGLE_FORM_CONFIG.openInModal) return;

    const style = document.createElement('style');
    style.textContent = `
        .form-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 10000;
            display: flex;
            align-items: center;
            justify-content: center;
            animation: fadeIn 0.2s ease-out;
        }

        .form-modal-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(4px);
        }

        .form-modal-content {
            position: relative;
            width: 90%;
            max-width: 640px;
            height: 80vh;
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
            animation: slideUp 0.3s ease-out;
        }

        .form-modal-close {
            position: absolute;
            top: 10px;
            right: 10px;
            width: 40px;
            height: 40px;
            border: none;
            background: rgba(0, 0, 0, 0.6);
            color: white;
            font-size: 28px;
            line-height: 1;
            border-radius: 50%;
            cursor: pointer;
            transition: background 0.2s;
            z-index: 10;
        }

        .form-modal-close:hover {
            background: rgba(0, 0, 0, 0.8);
        }

        .form-iframe {
            width: 100%;
            height: 100%;
            border: none;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes slideUp {
            from { 
                opacity: 0;
                transform: translateY(30px);
            }
            to { 
                opacity: 1;
                transform: translateY(0);
            }
        }

        @media (max-width: 736px) {
            .form-modal-content {
                width: 95%;
                height: 90vh;
            }
        }
    `;

    document.head.appendChild(style);
}

// Inject modal styles if needed
injectModalStyles();
