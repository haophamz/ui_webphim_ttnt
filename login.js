// Toggle password
        document.getElementById('togglePassword').addEventListener('click', function () {
            const pwd = document.getElementById('password');
            const icon = this.querySelector('i');
            if (pwd.type === 'password') {
                pwd.type = 'text';
                icon.classList.replace('fa-eye', 'fa-eye-slash');
            } else {
                pwd.type = 'password';
                icon.classList.replace('fa-eye-slash', 'fa-eye');
            }
        });

        // Login demo
        document.getElementById('loginForm').addEventListener('submit', function (e) {
            e.preventDefault();
            const btn = document.querySelector('.btn-submit');
            btn.innerHTML = `<i class="fas fa-spinner fa-spin"></i> ĐANG KIỂM TRA...`;
            btn.disabled = true;

            setTimeout(() => {
                btn.style.background = 'linear-gradient(90deg, #10b981, #34d399)';
                btn.innerHTML = `✅ ĐĂNG NHẬP THÀNH CÔNG`;
                setTimeout(() => alert('🎬 Chào mừng bạn đến với PhimHayOK!'), 800);
            }, 1600);
        });