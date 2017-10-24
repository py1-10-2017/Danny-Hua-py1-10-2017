SELECT users.first_name AS user_firstname, users.last_name AS user_lastname, friends.first_name AS friend_firstname, friends.last_name AS friend_lastname FROM users
LEFT JOIN friendships
ON users.id = friendships.user_id
LEFT JOIN users AS friends
ON friends.id = friendships.friend_id;