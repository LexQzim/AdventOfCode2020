public class Instruction
{
    public string type;
    public int value;
    public bool used;

    public Instruction(string type, int value)
    {
        this.type = type;
        this.value = value;
        used = false;
    }
}