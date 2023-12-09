function showDeleteModal(produkId) {
  const productName = document.querySelector(`#deleteModalText`);
  productName.textContent = `Anda yakin ingin menghapus produk dengan ID ${produkId}?`;

  const deleteButton = document.querySelector('#confirmDelete');
  deleteButton.dataset.id = produkId;

  const modalOverlay = document.querySelector('#deleteModal');
  modalOverlay.classList.remove('hidden');
}

function hideDeleteModal() {
  const modalOverlay = document.querySelector('#deleteModal');
  modalOverlay.classList.add('hidden');
}

function deleteProduct() {
  const productId = document.querySelector('#confirmDelete').dataset.id;

  fetch(`/hapus/${productId}`, {
    method: 'DELETE',
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
      'Content-Type': 'application/json',
    },
  })
    .then(response => {
      if (response.status === 200) {
        const successModal = document.querySelector('#successModal');
        hideDeleteModal()
        successModal.classList.remove('hidden');
        return response.json()
      } else if (!response.ok) {
        hideDeleteModal()
        throw new Error(`HTTP error! Status: ${response.status}`);
      } else {
        return response.json();
      }
    })
    .then(data => {
      console.log(data);
      successModal.classList.remove('hidden');
      if (data && data.message) {

        const successText = document.querySelector('#successModalText');
        successText.textContent = data.message;

        const successModal = document.querySelector('#successModal');
        hideDeleteModal()
      } else {
        console.error('Invalid response format:', data);
      }
    })
    .catch(error => console.error('Error:', error));
}

function hideSuccessModal() {
  const successModal = document.querySelector('#successModal');
  successModal.classList.add('hidden');

  location.reload();
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}