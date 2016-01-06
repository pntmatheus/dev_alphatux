$(document).ready(function() {
      $('#id_codigo').keypress(function(key) {
				if(key.charCode > 57) return false;
			});

      function remove_caracteres(valor) {
            return valor.replace(/[\.|\-|\/]/g, '');
      }

      function cpf_part_1(valor) {
            valor = valor.substring(0,3) + "." + valor.substring(3,6);
            return valor;
      }

      function cpf_part_2(valor) {
            valor = cpf_part_1(valor) + "." + valor.substring(6,9);
            return valor;
      }

      function cpf_part_3(valor) {
            valor = cpf_part_2(valor) + "-" + valor.substring(9);
            return valor;
      }

      function cnpj_part_1(valor) {
            valor = valor.substring(0,2) + "." + valor.substring(2,5) + "." + valor.substring(5,8) + "/" + valor.substring(8,12);
            return valor;
      }
      function cnpj_part_2(valor) {
            valor = cnpj_part_1(valor) + "-" + valor.substring(12);
            return valor;
      }
      obj = $("#id_codigo");

      $(obj).keyup(function(){

        numeros = remove_caracteres(obj.val())
        tamanho = numeros.length;

        patt = /[-|\.|\/]$/g;

        if (patt.test(obj.val())) {
            obj.val(obj.val().replace(/[-|\.|\/]$/g, ""));
        }

        if (tamanho > 3 && tamanho < 7) {
            obj.val(cpf_part_1(numeros));
        } else {
            if (tamanho > 6 && tamanho < 10) {
                obj.val(cpf_part_2(numeros));
            }
            else {
                if (tamanho > 9 && tamanho < 12) {
                    obj.val(cpf_part_3(numeros));
                }
                else {
                    if (tamanho > 11 && tamanho < 13) {
                        obj.val(cnpj_part_1(numeros));
                    }
                    else {
                        if (tamanho >= 13) {
                            obj.val(cnpj_part_2(numeros));
                        }
                    }
                }
            }
        }


      });
});