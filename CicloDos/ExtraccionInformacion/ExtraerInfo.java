import java.net.*;
import java.io.*;
/**
 *
 * @author Nancy Espinosa
 */
public class ExtraerInfo {
    public static void main(String [] args) throws Exception{
        String rutaKtronix = "https://www.ktronix.com/computadores-tablets/computadores-portatiles/c/BI_104_KTRON";
        URL url = new URL(rutaKtronix);
        BufferedReader reader = new BufferedReader(new InputStreamReader(url.openStream()));
        String codigoFuente = "";
        String linea;
        while((linea = reader.readLine()) != null){
            codigoFuente = codigoFuente + linea;
        }
        reader.close();
        //System.out.println(codigoFuente);

        int posicionFinal, posicionInicial, ultimaPodicion;
        int inicioNombre;
        int lengFuente, lengModelo, lengMsjPrecio;
        String modelosNombre, msjModelo, modelo, msjPrecio, precio;
        msjModelo = "<input type=\"hidden\" name=\"productNamePost\" value=\"";
        msjPrecio = "name=\"productPostPrice\" value=\"";

        lengFuente = codigoFuente.length();
        lengModelo = msjModelo.length();
        lengMsjPrecio = msjPrecio.length();
        posicionInicial = 0;
        ultimaPodicion = codigoFuente.lastIndexOf(msjPrecio);
        
        
        while (posicionInicial != ultimaPodicion){
            posicionInicial = codigoFuente.indexOf(msjModelo, (posicionInicial+1));
            inicioNombre = posicionInicial + lengModelo;
            posicionFinal = codigoFuente.indexOf("\"/>",inicioNombre);

            modelo = codigoFuente.substring(inicioNombre, posicionFinal);
            System.out.println("Nombre del modelo: " + modelo);



            posicionInicial = codigoFuente.indexOf(msjPrecio, (posicionFinal+1));
            inicioNombre = posicionInicial + lengMsjPrecio;
            posicionFinal = codigoFuente.indexOf("\"/>",inicioNombre);

            precio = codigoFuente.substring(inicioNombre, posicionFinal);
            System.out.println("Valor del modelo: " + precio);

        } 
        
    }   
}