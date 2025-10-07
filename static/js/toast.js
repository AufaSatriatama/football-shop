function showToast(title, message = '', type = 'success', duration = 3000) {
    const toast = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    const toastIcon = document.getElementById('toast-icon');
    
    if (!toast) return;
    
    // Set content
    toastTitle.textContent = title;
    toastMessage.textContent = message;
    
    // Set icon and color based on type
    let iconClass = '';
    let bgClass = '';
    
    switch (type) {
        case 'success':
            iconClass = '✅';
            bgClass = 'bg-green-100 border border-green-300 text-green-800';
            break;
        case 'error':
            iconClass = '❌';
            bgClass = 'bg-red-100 border border-red-300 text-red-800';
            break;
        case 'warning':
            iconClass = '⚠️';
            bgClass = 'bg-yellow-100 border border-yellow-300 text-yellow-800';
            break;
        case 'info':
            iconClass = 'ℹ️';
            bgClass = 'bg-blue-100 border border-blue-300 text-blue-800';
            break;
        default:
            iconClass = 'ℹ️';
            bgClass = 'bg-gray-100 border border-gray-300 text-gray-800';
    }
    
    toastIcon.textContent = iconClass;
    toast.className = `fixed bottom-8 right-8 p-4 px-8 rounded-xl shadow-xl z-50 transition-all duration-300 flex items-center gap-4 ${bgClass}`;
    
    // Show toast
    toast.classList.remove('opacity-0', 'translate-y-64');
    toast.classList.add('opacity-100', 'translate-y-0');
    
    // Hide toast after duration
    setTimeout(() => {
        toast.classList.remove('opacity-100', 'translate-y-0');
        toast.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}