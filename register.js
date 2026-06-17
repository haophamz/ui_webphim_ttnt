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

        document.getElementById('toggleConfirmPassword').addEventListener('click', function () {
            const pwd = document.getElementById('confirmPassword');
            const icon = this.querySelector('i');
            if (pwd.type === 'password') {
                pwd.type = 'text';
                icon.classList.replace('fa-eye', 'fa-eye-slash');
            } else {
                pwd.type = 'password';
                icon.classList.replace('fa-eye-slash', 'fa-eye');
            }
        });

        // Form submit animation
        document.getElementById('registerForm').addEventListener('submit', function (e) {
            e.preventDefault();
            const btn = document.querySelector('.btn-submit');
            const originalText = btn.innerHTML;

            btn.innerHTML = `<i class="fas fa-spinner fa-spin"></i> ĐANG XỬ LÝ...`;
            btn.disabled = true;

            setTimeout(() => {
                btn.style.background = 'linear-gradient(90deg, #10b981, #34d399)';
                btn.innerHTML = `✅ ĐĂNG KÝ THÀNH CÔNG`;
                setTimeout(() => {
                    alert('🎉 Chào mừng bạn đã tham gia PhimHayOK!');
                    // window.location.href = 'login.html';
                }, 1000);
            }, 1600);
        });