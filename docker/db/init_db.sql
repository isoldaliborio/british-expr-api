-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema british_expressions
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema british_expressions
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `british_expressions` DEFAULT CHARACTER SET utf8 ;
USE `british_expressions` ;

-- -----------------------------------------------------
-- Table `british_expressions`.`expressions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `british_expressions`.`expressions` ;

CREATE TABLE IF NOT EXISTS `british_expressions`.`expressions` (
  `id_exp` INT NOT NULL AUTO_INCREMENT,
  `expression` VARCHAR(200) CHARACTER SET 'utf8' NOT NULL,
  `meaning` TEXT NULL,
  `uses_example` VARCHAR(50) NULL,
  `context` TEXT NULL,
  UNIQUE INDEX `id_exp_UNIQUE` (`id_exp` ASC) VISIBLE,
  PRIMARY KEY (`id_exp`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `british_expressions`.`tags`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `british_expressions`.`tags` ;

CREATE TABLE IF NOT EXISTS `british_expressions`.`tags` (
  `id_tag` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `tag` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_tag`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `british_expressions`.`tags_expressions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `british_expressions`.`tags_expressions` ;

CREATE TABLE IF NOT EXISTS `british_expressions`.`tags_expressions` (
  `id_tags_expressions` INT NOT NULL,
  `expressions_id_exp` INT NOT NULL,
  `tags_id_tag` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id_tags_expressions`),
  INDEX `fk_tags_expressions_expressions1_idx` (`expressions_id_exp` ASC) VISIBLE,
  INDEX `fk_tags_expressions_tags1_idx` (`tags_id_tag` ASC) VISIBLE,
  CONSTRAINT `fk_tags_expressions_expressions1`
    FOREIGN KEY (`expressions_id_exp`)
    REFERENCES `british_expressions`.`expressions` (`id_exp`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tags_expressions_tags1`
    FOREIGN KEY (`tags_id_tag`)
    REFERENCES `british_expressions`.`tags` (`id_tag`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
