<?php
$username = $_POST['username'];
$password = $_POST['password'];


if ($username === 'admin' && $password === 'password') 
	$response = array('success' => true, 'message' => 'Login successful');
} else {
	$response = array('success' => false, 'message' => 'Invalid username or password');
}

echo json_encode($response);
?>