// This exercise validates locally. No question or address is sent or stored.
const form = document.querySelector('#contact-form');
if (form) {
  const controls = form.querySelectorAll('input, textarea, button');
  controls.forEach(control => { control.disabled = false; });
  const email = document.querySelector('#email');
  const confirmation = document.querySelector('#confirm-email');
  const status = document.querySelector('#form-status');

  // Editing either email clears a previous mismatch message.
  [email, confirmation].forEach(input => {
    input.addEventListener('input', () => {
      confirmation.removeAttribute('aria-invalid');
      status.textContent = '';
    });
  });

  form.addEventListener('submit', event => {
    event.preventDefault();
    if (email.value.trim() !== confirmation.value.trim()) {
      window.alert('Your email addresses do not match. Please check both fields.');
      confirmation.setAttribute('aria-invalid', 'true');
      status.textContent = 'Your email addresses do not match. Please check both fields.';
      confirmation.focus();
      return;
    }
    status.textContent = 'Your question passed the local checks. This practice form does not send or save your information.';
  });
}
