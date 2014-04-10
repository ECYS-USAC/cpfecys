<?php
session_name('11284b891395526f1b5c26d78dc798f4');
session_start();
// store session data
//$_SESSION['views']=1;
?>
<?php
//retrieve session data
//echo $_SESSION['_uid'];
//$_SESSION['_uid']=2;
if (!isset($_SESSION['_uid'])) return;
$mysqli = new mysqli("localhost", "root", "", "chamilo6");
if ($mysqli->connect_errno) {
    echo "Falló la conexión con MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}

$carnet = NULL;

/* crear una sentencia preparada */
if ($stmt = $mysqli->prepare("select username from user_user where id=?")) 
{

    /* ligar parámetros para marcadores */
    $stmt->bind_param("i", $_SESSION['_uid']);

    /* ejecutar la consulta */
    $stmt->execute();

    /* ligar variables de resultado */
    $stmt->bind_result($carnet);

    /* obtener valor */
    $stmt->fetch();

    /* cerrar sentencia */
    $stmt->close();
}else{
	echo "Falló laejecucion: (" . $mysqli->errno . ") " . $mysqli->error;
}
$mysqli->close();
//echo $carnet;

$mysqli = new mysqli("localhost", "root", "", "cpfecys");
if ($mysqli->connect_errno) {
    echo "Falló la conexión con MySQL: (" . $mysqli->connect_err . ")" . $mysqli->connect_error;
}

$token = sha1($carnet . time());
/* crear una sentencia preparada */
if ($stmt = $mysqli->prepare('update auth_user set uv_token=? where username=?')){

    /* ligar parámetros para marcadores */
    $stmt->bind_param('ss', $token, $carnet);
//    $stmt->bind_param('s', $username);

    /* ejecutar la consulta */
    if(!$stmt->execute()){
		echo "Fail";
	}

    $stmt->close();

}else{
	echo "Fallo la ejecucion " . $mysqli->errno . " error: " . $mysqli->error;
	return;
}
$mysqli->close();
//echo $token;

$ret = array();
$ret['token'] = $token;
$ret['uid'] = $_SESSION['_uid'];
//$ret['carnet'] = $carnet;

echo json_encode($ret);

?>

