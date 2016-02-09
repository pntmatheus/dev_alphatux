$(document).ready(function() {
      function remove_caracteres(valor) {
            return valor.replace(/[\.|\(\)\-|\/]/g, '');
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

      function telefone_part_1(valor) {
            valor = "(" + valor.substring(0,2) + ")" + valor.substring(2,6);
            return valor;
      }

      function telefone_part_2(valor) {
            valor = telefone_part_1(valor) + "-" + valor.substring(6,10);
            return valor;
      }

      function telefone_digito_mais(valor) {
            valor = "(" + valor.substring(0,2) + ")" + valor.substring(2,7) + "-" + valor.substring(7,11);
            return valor;
      }

      function mascara_telefone(tamanho, numeros) {
        if (tamanho > 1 && tamanho < 7) {
            return telefone_part_1(numeros);
        } else {
            if (tamanho > 6 && tamanho < 11) {
                return telefone_part_2(numeros);
            }
            else {
                if(tamanho == 11) {
                    return telefone_digito_mais(numeros);
                }
                else {
                    return numeros;
                }
            }
        }
      }

      patt = /[-|\.|\/]$/g;

      obj = $("#id_codigo");

      telefone1_obj = $("#id_telefone1");
      telefone2_obj = $("#id_telefone2");

      /* Inserir somente números */

      obj.keypress(function(key) {
				if(key.charCode > 57) return false;
			});

      telefone1_obj.keypress(function(key) {
				if(key.charCode > 57) return false;
			});

	  telefone2_obj.keypress(function(key) {
				if(key.charCode > 57) return false;
			});

      /***  Função para CPF/CNPJ ***/

      $(obj).keyup(function(){

        numeros = remove_caracteres(obj.val())
        tamanho = numeros.length;



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



      /*** Telefone 1 ***/

      $(telefone1_obj).keyup(function(){

        if (patt.test(telefone1_obj.val())) {
            telefone1_obj.val(telefone1_obj.val().replace(/[-|\.|\/]$/g, ""));
        }

        numeros = remove_caracteres(telefone1_obj.val())
        tamanho = numeros.length;

        telefone1_obj.val(mascara_telefone(tamanho, numeros));

      });

      /*** Telefone 2 ***/

      $(telefone2_obj).keyup(function(){

        if (patt.test(telefone2_obj.val())) {
            telefone2_obj.val(telefone2_obj.val().replace(/[-|\.|\/]$/g, ""));
        }

        numeros = remove_caracteres(telefone2_obj.val())
        tamanho = numeros.length;

        telefone2_obj.val(mascara_telefone(tamanho, numeros));

      });
});