import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.FlowPane;
import javafx.stage.Stage;

public class ParityCheckApplet extends Application {
    
    private TextField binaryInputField;
    private Button checkButton;
    private Label resultLabel;

    @Override
    public void start(Stage primaryStage) {
        FlowPane root = new FlowPane();
        root.setHgap(10);
        root.setVgap(10);

        //Binary input field
        binaryInputField = new TextField();
        binaryInputField.setPromptText("Enter Binary Data");
        root.getChildren().addAll(new Label("Enter Binary Data: "), binaryInputField);

        //Check button
        checkButton = new Button("Check Parity");
        checkButton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                String binaryData = binaryInputField.getText().trim();

                //Validate binary input
                if (!binaryData.matches("[01]+")) {
                    resultLabel.setText("Invalid binary input! Please enter a valid binary sequence (0s and 1s only).");
                    return;
                }

                //Calculate Parity
                int countOnes = binaryData.replaceAll("0", "").length();
                String parity = (countOnes % 2 == 0) ? "even" : "odd";
                
                //Display result
                resultLabel.setText("Parity: " + parity + " (" + countOnes + " ones)");
            }
        });
        root.getChildren().add(checkButton);

        //Result label
        resultLabel = new Label("");
        root.getChildren().add(resultLabel);
        

        Scene scene = new Scene(root, 300, 150);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Parity Check Applet");
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
