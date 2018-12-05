
package com.example.welcome.recyclerview;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class Properties {

    @SerializedName("foo")
    @Expose
    private Foo foo;
    @SerializedName("bar")
    @Expose
    private Bar bar;
    @SerializedName("baz")
    @Expose
    private Baz baz;

    public Foo getFoo() {
        return foo;
    }

    public void setFoo(Foo foo) {
        this.foo = foo;
    }

    public Bar getBar() {
        return bar;
    }

    public void setBar(Bar bar) {
        this.bar = bar;
    }

    public Baz getBaz() {
        return baz;
    }

    public void setBaz(Baz baz) {
        this.baz = baz;
    }

}
