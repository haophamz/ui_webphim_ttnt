// Form submit animation
        document.getElementById('forgotForm').addEventListener('submit', function (e) {
            e.preventDefault();
            const btn = document.querySelector('.btn-submit');
            const originalText = btn.innerHTML;

            btn.innerHTML = `<i class="fas fa-spinner fa-spin"></i> ĐANG GỬI...`;
            btn.disabled = true;

            setTimeout(() => {
                btn.style.background = 'linear-gradient(90deg, #10b981, #34d399)';
                btn.innerHTML = `✅ ĐÃ GỬI LIÊN KẾT!`;
                
                setTimeout(() => {
                    alert('📧 Liên kết khôi phục mật khẩu đã được gửi đến email của bạn!');
                    // window.location.href = 'login.html';
                }, 1200);
            }, 1500);
        });