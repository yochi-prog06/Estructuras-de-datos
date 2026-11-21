module lab.flotavehicular {
    requires javafx.controls;
    requires javafx.fxml;
    opens lab.flotavehicular.controller to javafx.fxml;
    exports lab.flotavehicular;
    exports lab.flotavehicular.model;
}
