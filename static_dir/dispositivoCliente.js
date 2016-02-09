$(document).ready(function() {
      function remove_caracteres(valor) {
            return valor.replace(/[\.|:\(\)\-|\/]/g, '');
      }

      function format_mac(valor, tamanho, tecla) {

            patt = /:$/g;
            dois_pontos = (valor.match(/:/g) || [] ).length;
            tamanho_total = valor.length;
            var separador = ":";
            if (patt.test(valor)) {
                valor = valor.replace(/:$/, "");
            }
            else {
                if ((dois_pontos == 1 && tamanho == 5) || (dois_pontos == 2 && tamanho == 7) || (dois_pontos == 3 && tamanho == 9) || (dois_pontos == 4 && tamanho == 11)) {
                    tres_ultimos = valor.substr(tamanho_total-3, 3);
                    valor = valor.replace(tres_ultimos, tres_ultimos.substr(0,2) + ":" + tres_ultimos.substr(2));

                }
                else {
                    if (tamanho%2 == 0 && tamanho != 0 && tamanho != 12) {
                        if (tecla != 0) {
                            valor = valor + separador;
                        }
                    }
                }
            }

            return valor.toUpperCase();
      }

      patt = /[-|\.|\/]$/g;

      obj = $("#id_mac_wan");

      obj.keypress(function(key) {
		    char = key.charCode;
	  });

      $(obj).keyup(function(){



        sem_ponto = remove_caracteres(obj.val())
        tamanho = sem_ponto.length;
        valor = obj.val();

        obj.val(format_mac(valor, tamanho, char));
      });
});