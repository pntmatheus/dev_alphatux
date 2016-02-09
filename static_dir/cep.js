$(document).ready(function() {
      function remove_caracteres(valor) {
            return valor.replace(/[\.|:\(\)\-|\/]/g, '');
      }

      function format_cep(cep) {

            sem_ponto = remove_caracteres(cep);
            tamanho = sem_ponto.length;

            patt = /-$/g;

            if (patt.test(cep)) {
                valor = valor.replace(/-$/, "");
            }
            else {
                if (tamanho > 5) {
                    valor = sem_ponto.substr(0,5) + "-" + sem_ponto.substr(5);
                }
            }

            return valor;
      }

      patt = /[-|\.|\/]$/g;

      obj = $("#id_codigo");

      $(obj).keyup(function(){

        valor = obj.val();

        obj.val(format_cep(valor));
      });
});