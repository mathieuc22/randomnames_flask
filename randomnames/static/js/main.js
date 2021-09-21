document.addEventListener('DOMContentLoaded', () => {

  // select the checkbox to add query param
  const lowerCheckbox = document.querySelector('input[id="lower"]');
  lowerCheckbox.onchange = function () {
    fetchNamesJSON().then(names => {
      document.querySelector('#randomname').value = names;
      document.title = names;
    });
  };

  // select the checkbox to add query param
  const separatorInput = document.querySelector('input[id="separator"]');
  separatorInput.onchange = function () {
    fetchNamesJSON().then(names => {
      document.querySelector('#randomname').value = names;
      document.title = names;
    });
  };
  const separatorCheckbox = document.querySelector('input[id="noseparator"]');
  separatorCheckbox.onchange = function () {
    separatorInput.disabled = !separatorInput.disabled
    fetchNamesJSON().then(names => {
      document.querySelector('#randomname').value = names;
      document.title = names;
    });
  };

  // select the checkbox to add query param
  const numberRange = document.querySelector('input[id="number"]');
  numberRange.onchange = function () {
    fetchNamesJSON().then(names => {
      document.querySelector('#randomname').value = names;
      document.title = names;
    });
  };

  document.querySelector('#refresh').onclick = () => {

    fetchNamesJSON().then(names => {
      document.querySelector('#randomname').value = names;
      document.title = names;
    });
    
  };

  document.querySelector('#copy').onclick = () => {
    document.querySelector('#randomname').select();
    document.querySelector('#randomname').setSelectionRange(0, 99999);
    document.execCommand('copy');
  };
});

// reusable fetch function for randomnames
async function fetchNamesJSON() {

  // add the base url
  let url = new URL(window.location.protocol + '//' + window.location.host + '/api/randomnames');
  let params = {}

  // select the checkbox to add query param
  const lowerCheckbox = document.querySelector('input[id="lower"]');
  if (lowerCheckbox.checked) {
    params.lower = 'True'
  }
  const separatorCheckbox = document.querySelector('input[id="noseparator"]');
  const separatorInput = document.querySelector('input[id="separator"]');
  if (separatorCheckbox.checked) {
    params.separator = ''
  } else if (separatorInput.value) {
    params.separator = separatorInput.value
  }
  const numberRange = document.querySelector('input[id="number"]');
  if (numberRange.value) {
    params.number = numberRange.value
  }

  url.search = new URLSearchParams(params).toString();
  
  const response = await fetch(url);
  if (!response.ok) {
    const message = `An error has occured: ${response.status}`;
    throw new Error(message);
  };
  const names = await response.json();
  return names.name;
}
