```javascript

  let cookie = document.cookie
  let csrfToken = cookie.substring(cookie.indexOf('=') + 1)

var element = document.querySelector(".form");
element.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {

    $.ajax({
      type:"POST",
      url: "{% url 'bakim-rapor' %}",
      data:{
        deneme:"deneme",
      },
      headers: {
        'X-CSRFToken': csrfToken
      },
      success: function(result){
        console.log(result.items);
        console.log("result.items");
      }
    }); 
    
    alert(event.key  + " " + event.which);
    event.preventDefault();
    }
});
```

<br> 

djangoda post isteği ile csrf token i de göndermek gerekiyor . Ajax isteği yapıyoruz yukarıdaki kod ile datayı headers da eklediğimiz csrf token ile gönderdiğimizde istek başarılı olacaktır
