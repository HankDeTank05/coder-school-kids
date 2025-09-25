using Godot;
using System;
using System.Numerics;
using System.Runtime.CompilerServices;
using Vector2 = Godot.Vector2;

public partial class Player : Area2D
{
    [Signal]
    public delegate void HitEventHandler();
    [Export]
    public int Speed = 400;

    public Vector2 ScreenSize;

    public override void _Ready()
    {
        ScreenSize = GetViewportRect().Size;
        Hide();

    }

    public override void _Process(double delta)
    {
        var velocity = Vector2.Zero;
        if (Input.IsActionPressed("move_right"))
        {
            velocity.X += 1;
        }
        if (Input.IsActionPressed("move_left"))
        {
            velocity.X -= 1;
        }
        if (Input.IsActionPressed("move_down"))
        {
            velocity.Y += 1;
        }
        if (Input.IsActionPressed("move_up"))
        {
            velocity.Y -= 1;
        }
        var playerSprite = GetNode<AnimatedSprite2D>("AnimatedSprite2D");
        if (velocity.Length() > 0)
        {
            velocity = velocity.Normalized() * Speed;
            playerSprite.Play();

        }
        else
        {
            playerSprite.Stop();
        }
        Position += velocity * (float)delta;
        Position = new Vector2(Mathf.Clamp(Position.X, 0, ScreenSize.X), Mathf.Clamp(Position.Y, 0, ScreenSize.Y));
        if (velocity.X != 0)
        {
            playerSprite.Animation = "walk";
            playerSprite.FlipV = false;
            playerSprite.FlipH = velocity.X < 0;
        }
        else if (velocity.Y != 0)
        {
            playerSprite.Animation = "up";
            playerSprite.FlipV = velocity.Y > 0;
        }
    }

    private void OnBodyEntered()
    {
        Hide();
        EmitSignal(SignalName.Hit);
        GetNode<CollisionShape2D>("CollisionShape2D").SetDeferred(CollisionShape2D.PropertyName.Disabled, true);

    }
    public void Start(Vector2 position)
    {
        Position = position;
        Show();
        GetNode<CollisionShape2D>("CollisionShape2D").Disabled = false;
    }
}
