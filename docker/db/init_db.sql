
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema british_expressions
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `british_expressions` ;

-- -----------------------------------------------------
-- Schema british_expressions
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `british_expressions` DEFAULT CHARACTER SET utf8 ;
USE `british_expressions` ;

-- -----------------------------------------------------
-- Table `british_expressions`.`roles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `british_expressions`.`roles` (
  `role_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) CHARACTER SET 'utf8' NOT NULL,
  PRIMARY KEY (`role_id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `british_expressions`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `british_expressions`.`users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(200) CHARACTER SET 'utf8' NOT NULL,
  `last_name` VARCHAR(200) CHARACTER SET 'utf8' NOT NULL,
  `email` VARCHAR(200) CHARACTER SET 'utf8' NOT NULL,
  `password` VARCHAR(200) CHARACTER SET 'utf8' NOT NULL,
  `role_id` INT NOT NULL,
  `active` TINYINT(1) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC) VISIBLE,
  INDEX `fk_user_roles1_idx` (`role_id` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  CONSTRAINT `fk_user_roles1`
    FOREIGN KEY (`role_id`)
    REFERENCES `british_expressions`.`roles` (`role_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `british_expressions`.`expressions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `british_expressions`.`expressions` (
  `expression_id` INT NOT NULL AUTO_INCREMENT,
  `expression` VARCHAR(200) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NOT NULL,
  `meaning` TEXT CHARACTER SET 'utf8' NOT NULL,
  `created_at` TIMESTAMP NOT NULL,
  `modified_at` TIMESTAMP NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`expression_id`),
  INDEX `fk_expressions_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_expressions_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `british_expressions`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `british_expressions`.`categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `british_expressions`.`categories` (
  `category_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) CHARACTER SET 'utf8' NOT NULL,
  PRIMARY KEY (`category_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `british_expressions`.`categories_expressions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `british_expressions`.`categories_expressions` (
  `category_expression_id` INT NOT NULL AUTO_INCREMENT,
  `category_id` INT NOT NULL,
  `expression_id` INT NOT NULL,
  PRIMARY KEY (`category_expression_id`),
  INDEX `fk_categories_expressions_categories1_idx` (`category_id` ASC) VISIBLE,
  INDEX `fk_categories_expressions_expressions1_idx` (`expression_id` ASC) VISIBLE,
  CONSTRAINT `fk_categories_expressions_categories1`
    FOREIGN KEY (`category_id`)
    REFERENCES `british_expressions`.`categories` (`category_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_categories_expressions_expressions1`
    FOREIGN KEY (`expression_id`)
    REFERENCES `british_expressions`.`expressions` (`expression_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `british_expressions`.`tags`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `british_expressions`.`tags` (
  `tag_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) CHARACTER SET 'utf8' NOT NULL,
  PRIMARY KEY (`tag_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `british_expressions`.`user_tags`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `british_expressions`.`user_tags` (
  `expression_id` INT NOT NULL,
  `tag_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  INDEX `fk_tag_expression_user_expressions1_idx` (`expression_id` ASC) VISIBLE,
  INDEX `fk_user_tags_tags1_idx` (`tag_id` ASC) VISIBLE,
  PRIMARY KEY (`expression_id`, `tag_id`, `user_id`),
  INDEX `fk_user_tags_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_tag_expression_user_expressions1`
    FOREIGN KEY (`expression_id`)
    REFERENCES `british_expressions`.`expressions` (`expression_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_tags_tags1`
    FOREIGN KEY (`tag_id`)
    REFERENCES `british_expressions`.`tags` (`tag_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_tags_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `british_expressions`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `british_expressions`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `british_expressions`.`favorites` (
  `expression_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  INDEX `fk_favorites_expressions1_idx` (`expression_id` ASC) VISIBLE,
  INDEX `fk_favorites_user_tags1_idx` (`user_id` ASC) VISIBLE,
  PRIMARY KEY (`expression_id`, `user_id`),
  CONSTRAINT `fk_favorites_expressions1`
    FOREIGN KEY (`expression_id`)
    REFERENCES `british_expressions`.`expressions` (`expression_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favorites_user_tags1`
    FOREIGN KEY (`user_id`)
    REFERENCES `british_expressions`.`user_tags` (`expression_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `british_expressions`.`examples`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `british_expressions`.`examples` (
  `example_id` INT NOT NULL AUTO_INCREMENT,
  `example` TEXT CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NOT NULL,
  `expressions_expression_id` INT NOT NULL,
  PRIMARY KEY (`example_id`),
  INDEX `fk_examples_expressions1_idx` (`expressions_expression_id` ASC) VISIBLE,
  CONSTRAINT `fk_examples_expressions1`
    FOREIGN KEY (`expressions_expression_id`)
    REFERENCES `british_expressions`.`expressions` (`expression_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
