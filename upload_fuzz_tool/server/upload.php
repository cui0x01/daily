<?php

if( isset( $_FILES[ 'uploaded' ] ) ) {
	
	$target_path  = "uploads/".basename( $_FILES[ 'uploaded' ][ 'name' ] );

    if( !move_uploaded_file( $_FILES[ 'uploaded' ][ 'tmp_name' ], $target_path ) ) {

        echo '<pre>Your image was not uploaded.</pre>';
    }
    else {

        echo "<pre>{$target_path} succesfully uploaded!</pre>";
    }
}

?> 