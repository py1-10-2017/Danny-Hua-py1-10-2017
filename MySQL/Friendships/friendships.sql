-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema Friendships
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Friendships
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Friendships` DEFAULT CHARACTER SET utf8 ;
USE `Friendships` ;

-- -----------------------------------------------------
-- Table `Friendships`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Friendships`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Friendships`.`friendships`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Friendships`.`friendships` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `friend_id` INT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_friendships_users_idx` (`user_id` ASC),
  INDEX `fk_friendships_users1_idx` (`friend_id` ASC),
  CONSTRAINT `fk_friendships_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `Friendships`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_friendships_users1`
    FOREIGN KEY (`friend_id`)
    REFERENCES `Friendships`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
